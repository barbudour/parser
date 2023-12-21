# INumberContext.NumberObject - свойство
Объект, определяющий свойства номера и средства его хранения.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    INumberObject NumberObject { get; set; }
VB __Копировать
     Property NumberObject As INumberObject
    	Get
    	Set
C++ __Копировать
    property INumberObject^ NumberObject {
    	INumberObject^ get ();
    	void set (INumberObject^ value);
    }
F# __Копировать
     abstract NumberObject : INumberObject with get, set
#### Значение свойства
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[INumberContext - ](T_Tessa_Cards_Numbers_INumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
[Tessa.Platform.ObjectSealedException]
