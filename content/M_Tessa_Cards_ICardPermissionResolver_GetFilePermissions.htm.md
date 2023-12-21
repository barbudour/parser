# ICardPermissionResolver.GetFilePermissions - метод
Возвращает права доступа к прикреплённому к карточке файлу fileID.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     CardPermissionFlags GetFilePermissions(
    	Guid fileID
    )
VB __Копировать
     Function GetFilePermissions ( 
    	fileID As Guid
    ) As CardPermissionFlags
C++ __Копировать
     CardPermissionFlags GetFilePermissions(
    	Guid fileID
    )
F# __Копировать
     abstract GetFilePermissions : 
            fileID : Guid -> CardPermissionFlags 
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор прикреплённого к карточке файла.
#### Возвращаемое значение
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)  
Права доступа к файлу, прикреплённому к карточке.
##  __См. также
#### Ссылки
[ICardPermissionResolver - ](T_Tessa_Cards_ICardPermissionResolver.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
