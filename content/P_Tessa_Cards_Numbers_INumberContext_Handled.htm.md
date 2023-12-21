# INumberContext.Handled - свойство
Признак того, что действие было успешно обработано, если свойство
[Tessa.Cards.Numbers.INumberContext.CanHandle] возвращает true. В противном
случае значене равно false, что следует трактовать как "информация о
выполнении неизвестна".
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool Handled { get; set; }
VB __Копировать
     Property Handled As Boolean
    	Get
    	Set
C++ __Копировать
    property bool Handled {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     abstract Handled : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[INumberContext - ](T_Tessa_Cards_Numbers_INumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
[Tessa.Platform.ObjectSealedException]
