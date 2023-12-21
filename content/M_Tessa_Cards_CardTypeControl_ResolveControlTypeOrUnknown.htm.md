# CardTypeControl.ResolveControlTypeOrUnknown - метод
Возвращает тип элемента управления
[CardControlType](T_Tessa_Cards_CardControlType.htm) из реестра
зарегистрированных типов. Если тип отсутствует, то возвращается новый
экземпляр типа с указанием идентификатора и имени
[UnknownName](F_Tessa_Cards_CardControlType_UnknownName.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static CardControlType ResolveControlTypeOrUnknown(
    	Guid typeID
    )
VB __Копировать
     Protected Shared Function ResolveControlTypeOrUnknown ( 
    	typeID As Guid
    ) As CardControlType
C++ __Копировать
     protected:
    static CardControlType^ ResolveControlTypeOrUnknown(
    	Guid typeID
    )
F# __Копировать
     static member ResolveControlTypeOrUnknown : 
            typeID : Guid -> CardControlType 
#### Параметры
typeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор искомого типа элемента управления.
#### Возвращаемое значение
[CardControlType](T_Tessa_Cards_CardControlType.htm)  
Объект [CardControlType](T_Tessa_Cards_CardControlType.htm), описывающий тип
элемента управления.
##  __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
