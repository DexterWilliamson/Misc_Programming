# read_running_times.py
# Chapter 6.2


def main():
    # Open the video_times.txt file for reading.
    video_file = open('video_times.txt', 'r')

    # Initialize an accumulator to 0.0
    total = 0.0

    # Initialize a variable to keep count of the videos.
    count = 0

    print('Here are the running times for each video:')

    # Get the values from the file and total them.


    # BUG #1: Missing colon
    #for line in video_file
    for line in video_file:

        
        # Convert a line to a float.
        run_time = float(line)

        # Add 1 to the count variable.
        count += 1

        # Display the time.
        print('Video #', count, ': ', run_time, sep='')

        # Add the time to total.


        # BUG #2: run_time should be used here, not count
        # This is an example of a logic error
        #total += count
        total += run_time
        

    # Close the file
    video_file.close()

    # Display the total of the running times.
    print('The total running time is', total, 'seconds.')

    # Call the main function


    # BUG #3: main() should be called outside of the def main(): block
    #main()
main()
