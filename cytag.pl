#!/bin/perl -w
use strict;
my $working;
my @rules;
my $rulecount=0;
my $temp;
my $temp2;
my $doubling=0;
# If a Y is given as the first argument, double each element of the output to
# show the similarity to system 5
$ARGV[0]eq'Y' and do{$doubling=1; shift @ARGV;};
# Read from file
$ARGV[0]eq'F' and do{
 shift @ARGV;
 my $file = shift @ARGV;
 local $/ = undef;
 open INFILE, $file;
 @ARGV = split(' ',<INFILE>);
 close INFILE;
};
$|=1;
# Load the working string
$working=shift @ARGV;
chomp $working;
# Load the rules
for my $e (@ARGV)
{
 chomp $e;
 $e eq '""' and $e = '';
 $rules[$rulecount++]=$e;
}
while($working ne '')
{
 # Remove and print the first element of the working string
 $temp=substr $working,0,1,'';
 print $temp;
 $doubling and print $temp;
 push @rules, ($temp2 = shift @rules);
 $temp eq '1' and $working .= $temp2;
}
print "\n";