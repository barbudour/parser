# CardTypeBlock.Controls - свойство
Объекты содержимого, определяющие внешний вид карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeControl> Controls { get; set; }
VB __Копировать
     Public Property Controls As SealableObjectList(Of CardTypeControl)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeControl^>^ Controls {
    	SealableObjectList<CardTypeControl^>^ get ();
    	void set (SealableObjectList<CardTypeControl^>^ value);
    }
F# __Копировать
     member Controls : SealableObjectList<CardTypeControl> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeBlock - ](T_Tessa_Cards_CardTypeBlock.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
