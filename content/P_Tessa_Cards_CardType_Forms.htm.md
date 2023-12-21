# CardType.Forms - свойство
Альтернативные варианты пользовательского интерфейса для редактирования
карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeNamedForm> Forms { get; set; }
VB __Копировать
     Public Property Forms As SealableObjectList(Of CardTypeNamedForm)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeNamedForm^>^ Forms {
    	SealableObjectList<CardTypeNamedForm^>^ get ();
    	void set (SealableObjectList<CardTypeNamedForm^>^ value);
    }
F# __Копировать
     member Forms : SealableObjectList<CardTypeNamedForm> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeNamedForm](T_Tessa_Cards_CardTypeNamedForm.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardType - ](T_Tessa_Cards_CardType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
