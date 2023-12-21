# CardTypeEntryControl.RequiredText - свойство
Текст, отображаемый при отсутствии значения для контрола, значение которого
должно быть обязательно задано.
Если задано null или пустая строка, то используется строка из валидатора или
строка по умолчанию.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string RequiredText { get; set; }
VB __Копировать
     Public Property RequiredText As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ RequiredText {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member RequiredText : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeEntryControl - ](T_Tessa_Cards_CardTypeEntryControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
