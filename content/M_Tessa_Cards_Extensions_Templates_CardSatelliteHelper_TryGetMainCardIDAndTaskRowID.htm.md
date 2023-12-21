# CardSatelliteHelper.TryGetMainCardIDAndTaskRowID - метод
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static (bool result, Guid? mainCardID, Guid? taskRowID) TryGetMainCardIDAndTaskRowID(
    	Card satellite
    )
VB __Копировать
     Public Shared Function TryGetMainCardIDAndTaskRowID ( 
    	satellite As Card
    ) As (result As Boolean, mainCardID As Guid?, taskRowID As Guid?)
C++ __Копировать
     public:
    static ValueTuple<bool, Nullable<Guid>, Nullable<Guid>> TryGetMainCardIDAndTaskRowID(
    	Card^ satellite
    )
F# __Копировать
     static member TryGetMainCardIDAndTaskRowID : 
            satellite : Card -> ValueTuple<bool, Nullable<Guid>, Nullable<Guid>> 
#### Параметры
satellite [Card](T_Tessa_Cards_Card.htm)
#### Возвращаемое значение
[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>,
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>
##  __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
