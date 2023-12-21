# ICardPermissionResolver.GetFieldPermissions(String, String) - метод
Возвращает права доступа к полю fieldName из секции sectionName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     CardPermissionFlags GetFieldPermissions(
    	string sectionName,
    	string fieldName
    )
VB __Копировать
     Function GetFieldPermissions ( 
    	sectionName As String,
    	fieldName As String
    ) As CardPermissionFlags
C++ __Копировать
     CardPermissionFlags GetFieldPermissions(
    	String^ sectionName, 
    	String^ fieldName
    )
F# __Копировать
     abstract GetFieldPermissions : 
            sectionName : string * 
            fieldName : string -> CardPermissionFlags 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля.
#### Возвращаемое значение
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)  
Права доступа к полю.
##  __Исключения
[System.ArgumentNullException]|  Параметры sectionName или fieldName равны
null.  
---|---  
## __См. также
#### Ссылки
[ICardPermissionResolver - ](T_Tessa_Cards_ICardPermissionResolver.htm)
[GetFieldPermissions -
перегрузка](Overload_Tessa_Cards_ICardPermissionResolver_GetFieldPermissions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[System.ArgumentNullException]
