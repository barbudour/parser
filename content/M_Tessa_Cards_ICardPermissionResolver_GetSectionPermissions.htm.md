# ICardPermissionResolver.GetSectionPermissions - метод
Возвращает права доступа к строкам или полям секции sectionName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     CardPermissionFlags GetSectionPermissions(
    	string sectionName
    )
VB __Копировать
     Function GetSectionPermissions ( 
    	sectionName As String
    ) As CardPermissionFlags
C++ __Копировать
     CardPermissionFlags GetSectionPermissions(
    	String^ sectionName
    )
F# __Копировать
     abstract GetSectionPermissions : 
            sectionName : string -> CardPermissionFlags 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции.
#### Возвращаемое значение
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)  
Права доступа к строкам секции.
##  __Исключения
[System.ArgumentNullException]|  Параметр sectionName равен null.  
---|---  
## __См. также
#### Ссылки
[ICardPermissionResolver - ](T_Tessa_Cards_ICardPermissionResolver.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[System.ArgumentNullException]
