# CardTypeForm.Blocks - свойство
Блоки типа карточки, определяющие внешний вид карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeBlock> Blocks { get; set; }
VB __Копировать
     Public Property Blocks As SealableObjectList(Of CardTypeBlock)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeBlock^>^ Blocks {
    	SealableObjectList<CardTypeBlock^>^ get ();
    	void set (SealableObjectList<CardTypeBlock^>^ value);
    }
F# __Копировать
     member Blocks : SealableObjectList<CardTypeBlock> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeForm - ](T_Tessa_Cards_CardTypeForm.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
