# NumberStorageLocation.ToNumberLocation - метод
Преобразует местоположение номера, указанное в текущем объекте, в объект типа
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public INumberLocation ToNumberLocation(
    	INumberLocationManager manager
    )
VB __Копировать
     Public Function ToNumberLocation ( 
    	manager As INumberLocationManager
    ) As INumberLocation
C++ __Копировать
     public:
    INumberLocation^ ToNumberLocation(
    	INumberLocationManager^ manager
    )
F# __Копировать
     member ToNumberLocation : 
            manager : INumberLocationManager -> INumberLocation 
#### Параметры
manager
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm)
     Объект, определяющий поведение созданного объекта [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm). 
#### Возвращаемое значение
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)  
Объект, реализующий интерфейс
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm) и содержащий
местоположение номера, указанное в текущем объекте.
## __См. также
#### Ссылки
[NumberStorageLocation - ](T_Tessa_Cards_Numbers_NumberStorageLocation.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
