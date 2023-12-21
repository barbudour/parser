# CardTypeTableControl.Form - свойство
Объект, описывающий пользовательский интерфейс для редактирования строки
коллекционной или древовидной секции.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTypeTableForm Form { get; set; }
VB __Копировать
     Public Property Form As CardTypeTableForm
    	Get
    	Set
C++ __Копировать
     public:
    property CardTypeTableForm^ Form {
    	CardTypeTableForm^ get ();
    	void set (CardTypeTableForm^ value);
    }
F# __Копировать
     member Form : CardTypeTableForm with get, set
#### Значение свойства
[CardTypeTableForm](T_Tessa_Cards_CardTypeTableForm.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeTableControl - ](T_Tessa_Cards_CardTypeTableControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
