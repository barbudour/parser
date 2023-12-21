# CardTypeControl.ToolTip - свойство
Текст всплывающей подсказки для элемента управления или null, если имя не
задано. При задании пустой строки или строки, состоящей из пробелов,
устанавливается значение null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string ToolTip { get; set; }
VB __Копировать
     Public Property ToolTip As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ ToolTip {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member ToolTip : string with get, set
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
