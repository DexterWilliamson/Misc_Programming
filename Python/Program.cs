using System;

namespace Pets
{
    class Pets
    {
        static void Main(string[] args)
        {

            Pet pet1 = new Pet("Shadow", "Jose", "Dog", 42.6);

            Console.WriteLine("Name: " + pet1.name);
            Console.WriteLine("Weight: " + pet1.weight);
            Console.WriteLine(pet1.getTag());

            Dog dog1 = new Dog("Daisy", "Kent", 23.4);

            Console.WriteLine("Name: " + dog1.name);
            Console.WriteLine("Weight: " + dog1.weight);
            Console.WriteLine(dog1.getTag());
            Console.WriteLine(dog1.bark(4));
        }

        class Dogs
        {


        }

        class Cats
        {


        }
    }


            
            



    
}
