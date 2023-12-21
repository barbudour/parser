# CardNumberLocation.TryCreate - метод
Создаёт объект
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm) по данным
из хеш-таблицы info. Возвращает null, если хеш-таблица не содержит всех
необходимых данных.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardNumberLocation TryCreate(
    	IDictionary<string, Object> info,
    	INumberLocationManager manager
    )
VB __Копировать
     Public Shared Function TryCreate ( 
    	info As IDictionary(Of String, Object),
    	manager As INumberLocationManager
    ) As CardNumberLocation
C++ __Копировать
     public:
    static CardNumberLocation^ TryCreate(
    	IDictionary<String^, Object^>^ info, 
    	INumberLocationManager^ manager
    )
F# __Копировать
     static member TryCreate : 
            info : IDictionary<string, Object> * 
            manager : INumberLocationManager -> CardNumberLocation 
#### Параметры
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Данные, по которым строится создаваемый объект. Обычно такие данные расположены в свойстве [Info](P_Tessa_Cards_Numbers_INumberLocation_Info.htm). 
manager
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm)
     Объект, определяющий поведение номера. Не может быть равен null. 
#### Возвращаемое значение
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm)  
Созданный объект или null, если заданная хеш-таблица не содержит всех
необходимых данных.
## __См. также
#### Ссылки
[CardNumberLocation - ](T_Tessa_Cards_Numbers_CardNumberLocation.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
