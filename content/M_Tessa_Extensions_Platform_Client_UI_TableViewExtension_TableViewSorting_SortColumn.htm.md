# TableViewSorting.SortColumn - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ListSortDirection? SortColumn(
    	string alias,
    	bool shiftDown,
    	bool descendingByDefault
    )
VB __Копировать
     Public Function SortColumn ( 
    	alias As String,
    	shiftDown As Boolean,
    	descendingByDefault As Boolean
    ) As ListSortDirection?
C++ __Копировать
     public:
    virtual Nullable<ListSortDirection^> SortColumn(
    	String^ alias, 
    	bool shiftDown, 
    	bool descendingByDefault
    ) sealed
F# __Копировать
     abstract SortColumn : 
            alias : string * 
            shiftDown : bool * 
            descendingByDefault : bool -> Nullable<ListSortDirection> 
    override SortColumn : 
            alias : string * 
            shiftDown : bool * 
            descendingByDefault : bool -> Nullable<ListSortDirection> 
#### Параметры
alias [String](https://learn.microsoft.com/dotnet/api/system.string)
shiftDown [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
descendingByDefault
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[ListSortDirection](https://learn.microsoft.com/dotnet/api/system.componentmodel.listsortdirection)>
#### Реализации
[IViewSorting.SortColumn(String, Boolean,
Boolean)](M_Tessa_UI_Views_IViewSorting_SortColumn.htm)  
##  __См. также
#### Ссылки
[TableViewSorting -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewSorting.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
