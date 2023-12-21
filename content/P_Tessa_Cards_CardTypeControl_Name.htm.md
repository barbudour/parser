# CardTypeControl.Name - свойство
Имя элемента управления или null, если имя не задано. При задании пустой
строки устанавливается значение null. Рекомендуется задавать имя, уникальное
для формы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string Name { get; set; }
VB __Копировать
     Public Property Name As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ Name {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member Name : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
