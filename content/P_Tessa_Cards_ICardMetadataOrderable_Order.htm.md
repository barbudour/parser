# ICardMetadataOrderable.Order - свойство
Порядок следования элемента, например, порядок отображения элемента в
интерфейсе карточки, если элемент может быть отображён в интерфейсе.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     int Order { get; set; }
VB __Копировать
     Property Order As Integer
    	Get
    	Set
C++ __Копировать
    property int Order {
    	int get ();
    	void set (int value);
    }
F# __Копировать
     abstract Order : int with get, set
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardMetadataOrderable - ](T_Tessa_Cards_ICardMetadataOrderable.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
