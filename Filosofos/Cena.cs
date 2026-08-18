using System;
using System.Collections.Generic;
using System.Threading;

// Clase 1
class Fork
{
    public int Id { get; }
    public object LockObject { get; }

    public Fork(int id)
    {
        Id = id;
        LockObject = new object();
    }
}

// Clase 2
class Philosopher
{
    private int id;
    private Fork izquierdo;
    private Fork derecho;

    private static Random random = new Random();
    private static object randomLock = new object();

    public Philosopher(int id, Fork izquierdo, Fork derecho)
    {
        this.id = id;
        this.izquierdo = izquierdo;
        this.derecho = derecho;
    }

    public void Piensa()
    {
        Console.WriteLine($"Filosofo {id} esta pensando");

        Thread.Sleep(TiempoAleatorio());
    }

    public void Come()
    {
        Fork primero;
        Fork segundo;

        if (id % 2 == 0)
        {
            primero = izquierdo;
            segundo = derecho;
        }
        else
        {
            primero = derecho;
            segundo = izquierdo;
        }

        lock (primero.LockObject)
        {
            Console.WriteLine(
                $"Filosofo {id} toma el tenedor {primero.Id}"
            );

            lock (segundo.LockObject)
            {
                Console.WriteLine(
                    $"Filosofo {id} toma el tenedor {segundo.Id}"
                );

                Console.WriteLine(
                    $"Filosofo {id} esta comiendo"
                );

                Thread.Sleep(TiempoAleatorio());
            }
        }

        Console.WriteLine(
            $"Filosofo {id} termino de comer"
        );
    }

    public void Run()
    {
        for (int i = 0; i < 3; i++)
        {
            Piensa();
            Come();
        }
    }

    private int TiempoAleatorio()
    {
        lock (randomLock)
        {
            return random.Next(100, 501);
        }
    }
}

// Clase 3
class MainApplication
{
    private const int N = 5;

    private List<Fork> tenedores;
    private List<Philosopher> filosofos;
    private List<Thread> threads;

    public MainApplication()
    {
        tenedores = new List<Fork>();
        filosofos = new List<Philosopher>();
        threads = new List<Thread>();
    }

    public void CrearTenedores()
    {
        for (int i = 0; i < N; i++)
        {
            Fork tenedor = new Fork(i);
            tenedores.Add(tenedor);
        }
    }

    public void CrearFilosofos()
    {
        for (int i = 0; i < N; i++)
        {
            Fork izquierdo = tenedores[i];
            Fork derecho = tenedores[(i + 1) % N];

            Philosopher filosofo = new Philosopher(
                i,
                izquierdo,
                derecho
            );

            filosofos.Add(filosofo);
        }
    }

    public void CrearThreads()
    {
        foreach (Philosopher filosofo in filosofos)
        {
            Thread thread = new Thread(filosofo.Run);
            threads.Add(thread);
        }
    }

    public void IniciarThreads()
    {
        foreach (Thread thread in threads)
        {
            thread.Start();
        }
    }

    public void EsperarThreads()
    {
        foreach (Thread thread in threads)
        {
            thread.Join();
        }
    }

    public void Ejecutar()
    {
        Console.WriteLine("Inicia la cena\n");

        CrearTenedores();
        CrearFilosofos();
        CrearThreads();
        IniciarThreads();
        EsperarThreads();

        Console.WriteLine("\nTodos terminaron");
    }

    public static void Main(string[] args)
    {
        MainApplication app = new MainApplication();
        app.Ejecutar();
    }
}