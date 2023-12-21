# NumberLocation - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberLocation(
    	NumberLocationType type,
    	INumberLocationManager manager,
    	Dictionary<string, Object> info = null
    )
VB __Копировать
     Public Sub New ( 
    	type As NumberLocationType,
    	manager As INumberLocationManager,
    	Optional info As Dictionary(Of String, Object) = Nothing
    )
C++ __Копировать
     public:
    NumberLocation(
    	NumberLocationType^ type, 
    	INumberLocationManager^ manager, 
    	Dictionary<String^, Object^>^ info = nullptr
    )
F# __Копировать
     new : 
            type : NumberLocationType * 
            manager : INumberLocationManager * 
            ?info : Dictionary<string, Object> 
    (* Defaults:
            let _info = defaultArg info null
    *)
    -> NumberLocation
#### Параметры
type [NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm)
     Тип местоположения номера. Не может быть равен null. 
manager
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm)
     Объект, определяющий поведение создаваемого объекта. Не может быть равен null. 
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Параметры местоположения или null, если параметры не требуются. 
## __См. также
#### Ссылки
[NumberLocation - ](T_Tessa_Cards_Numbers_NumberLocation.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
