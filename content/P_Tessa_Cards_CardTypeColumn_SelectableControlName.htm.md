# CardTypeColumn.SelectableControlName - свойство
Имя (алиас) контрола, который будет автоматически выбран при открытии строки
по двойному клику по ячейке в этой колонке, или null, если выделяемых
контролов нет.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string SelectableControlName { get; set; }
VB __Копировать
     Public Property SelectableControlName As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ SelectableControlName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member SelectableControlName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeColumn - ](T_Tessa_Cards_CardTypeColumn.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
