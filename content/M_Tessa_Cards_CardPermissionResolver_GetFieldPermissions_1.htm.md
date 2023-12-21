# CardPermissionResolver.GetFieldPermissions(String, String, Guid) - метод
Возвращает права доступа к полю fieldName из коллекционной или древовидной
секции sectionName и строки с идентификатором rowID.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardPermissionFlags GetFieldPermissions(
    	string sectionName,
    	string fieldName,
    	Guid rowID
    )
VB __Копировать
     Public Function GetFieldPermissions ( 
    	sectionName As String,
    	fieldName As String,
    	rowID As Guid
    ) As CardPermissionFlags
C++ __Копировать
     public:
    virtual CardPermissionFlags GetFieldPermissions(
    	String^ sectionName, 
    	String^ fieldName, 
    	Guid rowID
    ) sealed
F# __Копировать
     abstract GetFieldPermissions : 
            sectionName : string * 
            fieldName : string * 
            rowID : Guid -> CardPermissionFlags 
    override GetFieldPermissions : 
            sectionName : string * 
            fieldName : string * 
            rowID : Guid -> CardPermissionFlags 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля.
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор строки коллекционной или древовидной секции.
#### Возвращаемое значение
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)  
Права доступа к полю.
#### Реализации
[ICardPermissionResolver.GetFieldPermissions(String, String,
Guid)](M_Tessa_Cards_ICardPermissionResolver_GetFieldPermissions_1.htm)  
##  __Исключения
[System.ArgumentNullException]|  Параметры sectionName или fieldName равны
null.  
---|---  
## __См. также
#### Ссылки
[CardPermissionResolver - ](T_Tessa_Cards_CardPermissionResolver.htm)
[GetFieldPermissions -
перегрузка](Overload_Tessa_Cards_CardPermissionResolver_GetFieldPermissions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[System.ArgumentNullException]
