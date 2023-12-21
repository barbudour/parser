# CardCachingPermissionResolver.GetRowPermissions - метод
Возвращает права доступа к строке с идентификатором rowID из секции
sectionName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardPermissionFlags GetRowPermissions(
    	string sectionName,
    	Guid rowID
    )
VB __Копировать
     Public Function GetRowPermissions ( 
    	sectionName As String,
    	rowID As Guid
    ) As CardPermissionFlags
C++ __Копировать
     public:
    virtual CardPermissionFlags GetRowPermissions(
    	String^ sectionName, 
    	Guid rowID
    ) sealed
F# __Копировать
     abstract GetRowPermissions : 
            sectionName : string * 
            rowID : Guid -> CardPermissionFlags 
    override GetRowPermissions : 
            sectionName : string * 
            rowID : Guid -> CardPermissionFlags 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции.
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор строки.
#### Возвращаемое значение
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)  
Права доступа к строке.
#### Реализации
[ICardPermissionResolver.GetRowPermissions(String,
Guid)](M_Tessa_Cards_ICardPermissionResolver_GetRowPermissions.htm)  
##  __Исключения
[System.ArgumentNullException]|  Параметр sectionName равен null.  
---|---  
## __См. также
#### Ссылки
[CardCachingPermissionResolver -
](T_Tessa_Cards_CardCachingPermissionResolver.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[System.ArgumentNullException]
