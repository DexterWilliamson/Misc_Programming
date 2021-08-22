using System;
using System.Linq;

namespace Pets
{
    public class Dog : Pet
    {

        public Dog(String petName, String petOwner, Double petWeight, String petType = "dog")
            : base(petName, petOwner, petType, petWeight)
        {

            
            name = petName;
            owner = petOwner;
            weight = petWeight;

        }

        public string bark(int count)
        {
            string[] barky = new string[count];
            for (int i = 0; i < count; i++)
            {

                barky[i] = "Bark!";

            }
            Console.WriteLine(barky);
            
            return "";


        }
    }

}
