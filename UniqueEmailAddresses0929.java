class UniqueEmailAddresses0929 {
    public int numUniqueEmails(String[] emails) {

        // process and add it to hash set and then count the number of elements in the hash set
        Set<String> hashSet = new HashSet<String>();

        for (String email : emails) {
            String[] arr = email.split("@");
            String name = arr[0];
            // Ignore any chars past '+'
            name = name.split("\\+")[0];
            // Remove '.'s
            name = name.replaceAll("\\.", "");
            String domain = arr[1];
            hashSet.add((name+"@"+domain));
        }

        return hashSet.size();
    }
}
