# CardTypeParamControl.InnerControlType - свойство
Контрол, выводимый при отсутствии связи с параметром.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTypeControl InnerControlType { get; set; }
VB __Копировать
     Public Property InnerControlType As CardTypeControl
    	Get
    	Set
C++ __Копировать
     public:
    property CardTypeControl^ InnerControlType {
    	CardTypeControl^ get ();
    	void set (CardTypeControl^ value);
    }
F# __Копировать
     member InnerControlType : CardTypeControl with get, set
#### Значение свойства
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeParamControl - ](T_Tessa_Cards_CardTypeParamControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
