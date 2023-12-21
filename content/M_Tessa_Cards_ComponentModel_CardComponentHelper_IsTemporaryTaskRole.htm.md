# CardComponentHelper.IsTemporaryTaskRole - метод
Возвращает признак того, что роль с заданным идентификатором типа является или
заменена на временную роль задания и должна быть удалена после завершения
задания.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsTemporaryTaskRole(
    	Guid roleTypeID
    )
VB __Копировать
     Public Shared Function IsTemporaryTaskRole ( 
    	roleTypeID As Guid
    ) As Boolean
C++ __Копировать
     public:
    static bool IsTemporaryTaskRole(
    	Guid roleTypeID
    )
F# __Копировать
     static member IsTemporaryTaskRole : 
            roleTypeID : Guid -> bool 
#### Параметры
roleTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа роли.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если роль с заданным идентификатором типа является или заменена на
временную роль задания; false в противном случае.
## __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
