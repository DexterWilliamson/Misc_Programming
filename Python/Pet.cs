using System;
namespace Pets
{
    public class Pet
    {

        public string name, owner, type;

        public double weight;

        public Pet(String petName, String petOwner, String petType, Double petWeight)
        {

            name = petName;
            owner = petOwner;
            type = petType;
            weight = petWeight;

        }

        public string getTag()
        { 
            
           string tag = "If lost, call " ;

           return tag + owner; 
        }
    }
}
