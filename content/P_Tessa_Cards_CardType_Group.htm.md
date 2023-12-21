# CardType.Group - свойство
Название группы для типа карточки. Может быть равно null, если группа не
задана.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string Group { get; set; }
VB __Копировать
     Public Property Group As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ Group {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member Group : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardType - ](T_Tessa_Cards_CardType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
