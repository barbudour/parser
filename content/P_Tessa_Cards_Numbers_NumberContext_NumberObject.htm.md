# NumberContext.NumberObject - свойство
Объект, определяющий свойства номера и средства его хранения.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public INumberObject NumberObject { get; set; }
VB __Копировать
     Public Property NumberObject As INumberObject
    	Get
    	Set
C++ __Копировать
     public:
    virtual property INumberObject^ NumberObject {
    	INumberObject^ get () sealed;
    	void set (INumberObject^ value) sealed;
    }
F# __Копировать
     abstract NumberObject : INumberObject with get, set
    override NumberObject : INumberObject with get, set
#### Значение свойства
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
#### Реализации
[INumberContext.NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
[Tessa.Platform.ObjectSealedException]
