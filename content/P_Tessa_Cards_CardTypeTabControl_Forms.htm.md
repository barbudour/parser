# CardTypeTabControl.Forms - свойство
Список форм, выводимый во вкладках.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeTabControlForm> Forms { get; set; }
VB __Копировать
     Public Property Forms As SealableObjectList(Of CardTypeTabControlForm)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeTabControlForm^>^ Forms {
    	SealableObjectList<CardTypeTabControlForm^>^ get ();
    	void set (SealableObjectList<CardTypeTabControlForm^>^ value);
    }
F# __Копировать
     member Forms : SealableObjectList<CardTypeTabControlForm> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeTabControlForm](T_Tessa_Cards_CardTypeTabControlForm.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeTabControl - ](T_Tessa_Cards_CardTypeTabControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
