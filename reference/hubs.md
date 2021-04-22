# Hub infrastructure we currently manage

## Hub deployment repositories

Here's [a link to a table of currently-running hub deployment repositories](https://docs.google.com/spreadsheets/d/1cy10fLUhlXG3M_TLRdqinETQ6h0puEi8ovBYHDTu3Z0/edit?usp=sharing). The issues in those repositories contain the deliverables for each.

In addition, here's a view of that table for quick reference:

<div class="full-width">

```{csv-table}
:header-rows: 1
:file: ../tmp/repo-deploy-table.csv
```

</div>


## Running JupyterHubs

Below is a list of communities that we currently serve via the central [`pilot-hubs/` repository](https://github.com/2i2c-org/pilot-hubs).

<div class="full-width">

```{csv-table}
:header-rows: 1
:file: ../tmp/hub-table.csv
```

</div>



<!-- DataTables to make the table above look nice -->
<link rel="stylesheet"
      href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css">
<script type="text/javascript" 
        src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready( function () {
    $('table').DataTable();
} );
</script>