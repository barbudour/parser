# NumberContext.Cancel - свойство
Признак того, что действие должно быть отменено для
[Tessa.Cards.Numbers.INumberExtendable.NotifyBeforeEventAsync] или было
отменено для [Tessa.Cards.Numbers.INumberExtendable.NotifyAfterEventAsync]. По
умолчанию свойство равно false.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Cancel { get; set; }
VB __Копировать
     Public Property Cancel As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool Cancel {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract Cancel : bool with get, set
    override Cancel : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[INumberContext.Cancel](P_Tessa_Cards_Numbers_INumberContext_Cancel.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
[Tessa.Platform.ObjectSealedException]
