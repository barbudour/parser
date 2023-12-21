# CardControlType.CreateUnknown - метод
Создаёт объект, который неизвестен в реестре, т.е. возвращает
[IsUnknown](P_Tessa_Cards_CardControlType_IsUnknown.htm), равный true.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardControlType CreateUnknown(
    	Guid id
    )
VB __Копировать
     Public Shared Function CreateUnknown ( 
    	id As Guid
    ) As CardControlType
C++ __Копировать
     public:
    static CardControlType^ CreateUnknown(
    	Guid id
    )
F# __Копировать
     static member CreateUnknown : 
            id : Guid -> CardControlType 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор объекта, который неизвестен в реестре.
#### Возвращаемое значение
[CardControlType](T_Tessa_Cards_CardControlType.htm)  
Объект, который неизвестен в реестре.
##  __См. также
#### Ссылки
[CardControlType - ](T_Tessa_Cards_CardControlType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
