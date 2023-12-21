# INumberContext.Cancel - свойство
Признак того, что действие должно быть отменено для
[Tessa.Cards.Numbers.INumberExtendable.NotifyBeforeEventAsync] или было
отменено для [Tessa.Cards.Numbers.INumberExtendable.NotifyAfterEventAsync]. По
умолчанию свойство равно false.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool Cancel { get; set; }
VB __Копировать
     Property Cancel As Boolean
    	Get
    	Set
C++ __Копировать
    property bool Cancel {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     abstract Cancel : bool with get, set
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
