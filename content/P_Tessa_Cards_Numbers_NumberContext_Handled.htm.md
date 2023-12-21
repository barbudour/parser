# NumberContext.Handled - свойство
Признак того, что действие было успешно обработано, если свойство
[Tessa.Cards.Numbers.INumberContext.CanHandle] возвращает true. В противном
случае значене равно false, что следует трактовать как "информация о
выполнении неизвестна".
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Handled { get; set; }
VB __Копировать
     Public Property Handled As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool Handled {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract Handled : bool with get, set
    override Handled : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[INumberContext.Handled](P_Tessa_Cards_Numbers_INumberContext_Handled.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
[Tessa.Platform.ObjectSealedException]
