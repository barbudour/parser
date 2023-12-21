# CardTypeControl.EqualsByControlSettings - метод
Сравнивает сериализованные значения свойств
[ControlSettings](P_Tessa_Cards_CardTypeControl_ControlSettings.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool EqualsByControlSettings(
    	CardTypeControl control
    )
VB __Копировать
     Public Function EqualsByControlSettings ( 
    	control As CardTypeControl
    ) As Boolean
C++ __Копировать
     public:
    bool EqualsByControlSettings(
    	CardTypeControl^ control
    )
F# __Копировать
     member EqualsByControlSettings : 
            control : CardTypeControl -> bool 
#### Параметры
control [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)
    Объект, свойство [ControlSettings](P_Tessa_Cards_CardTypeControl_ControlSettings.htm) которого требуется сравнить со свойством текущего объекта.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если свойства равны; false в противном случае.
##  __Заметки
При сравнении объектов этим методом производится сериализация свойства
[ControlSettings](P_Tessa_Cards_CardTypeControl_ControlSettings.htm).
## __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
