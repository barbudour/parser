# CardInfoStorageObject.DynamicInfo - свойство
Объект, осуществляющий доступ к дополнительной пользовательской информации по
текущему объекту через позднее связывание свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Object DynamicInfo { get; }
VB __Копировать
     Public ReadOnly Property DynamicInfo As Object
    	Get
C++ __Копировать
     public:
    property Object^ DynamicInfo {
    	Object^ get ();
    }
F# __Копировать
     member DynamicInfo : Object with get
#### Значение свойства
[Object](https://learn.microsoft.com/dotnet/api/system.object)
##  __Заметки
Обращение к DynamicInfo немного быстрее, чем к Dynamic.Info за счёт
кэширования выражений средой DLR.
## __См. также
#### Ссылки
[CardInfoStorageObject - ](T_Tessa_Cards_CardInfoStorageObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
