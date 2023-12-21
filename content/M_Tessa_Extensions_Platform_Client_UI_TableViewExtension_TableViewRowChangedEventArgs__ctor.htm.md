# TableViewRowChangedEventArgs - конструктор
Инициализирует новый экземпляр класса
[TableViewRowChangedEventArgs](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public TableViewRowChangedEventArgs(
    	TableViewRowChangeType changeType,
    	ViewControlRowViewModel row,
    	CardRow cardRow,
    	Guid rowID,
    	CardRow ownedRow,
    	string ownedSectionName,
    	string changedFieldName
    )
VB __Копировать
     Public Sub New ( 
    	changeType As TableViewRowChangeType,
    	row As ViewControlRowViewModel,
    	cardRow As CardRow,
    	rowID As Guid,
    	ownedRow As CardRow,
    	ownedSectionName As String,
    	changedFieldName As String
    )
C++ __Копировать
     public:
    TableViewRowChangedEventArgs(
    	TableViewRowChangeType changeType, 
    	ViewControlRowViewModel^ row, 
    	CardRow^ cardRow, 
    	Guid rowID, 
    	CardRow^ ownedRow, 
    	String^ ownedSectionName, 
    	String^ changedFieldName
    )
F# __Копировать
     new : 
            changeType : TableViewRowChangeType * 
            row : ViewControlRowViewModel * 
            cardRow : CardRow * 
            rowID : Guid * 
            ownedRow : CardRow * 
            ownedSectionName : string * 
            changedFieldName : string -> TableViewRowChangedEventArgs
#### Параметры
changeType
[TableViewRowChangeType](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangeType.htm)
row
[ViewControlRowViewModel](T_Tessa_UI_Views_Content_ViewControlRowViewModel.htm)
cardRow [CardRow](T_Tessa_Cards_CardRow.htm)
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
ownedRow [CardRow](T_Tessa_Cards_CardRow.htm)
ownedSectionName
[String](https://learn.microsoft.com/dotnet/api/system.string)
changedFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string)
## __См. также
#### Ссылки
[TableViewRowChangedEventArgs -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowChangedEventArgs.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
