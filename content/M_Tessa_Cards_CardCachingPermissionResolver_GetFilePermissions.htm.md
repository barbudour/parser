# CardCachingPermissionResolver.GetFilePermissions - метод
Возвращает права доступа к прикреплённому к карточке файлу fileID.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardPermissionFlags GetFilePermissions(
    	Guid fileID
    )
VB __Копировать
     Public Function GetFilePermissions ( 
    	fileID As Guid
    ) As CardPermissionFlags
C++ __Копировать
     public:
    virtual CardPermissionFlags GetFilePermissions(
    	Guid fileID
    ) sealed
F# __Копировать
     abstract GetFilePermissions : 
            fileID : Guid -> CardPermissionFlags 
    override GetFilePermissions : 
            fileID : Guid -> CardPermissionFlags 
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор прикреплённого к карточке файла.
#### Возвращаемое значение
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)  
Права доступа к файлу, прикреплённому к карточке.
#### Реализации
[ICardPermissionResolver.GetFilePermissions(Guid)](M_Tessa_Cards_ICardPermissionResolver_GetFilePermissions.htm)  
##  __См. также
#### Ссылки
[CardCachingPermissionResolver -
](T_Tessa_Cards_CardCachingPermissionResolver.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
