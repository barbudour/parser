# CardValidationContext.ForceWarnings - свойство
Признак того, что валидаторы-предупреждения срабатывают даже в том случае,
если они не должны срабатывать, например, на клиенте. Это полезно, если
выполняется валидация на клиенте без валидации на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool ForceWarnings { get; set; }
VB __Копировать
     Public Property ForceWarnings As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool ForceWarnings {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract ForceWarnings : bool with get, set
    override ForceWarnings : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[ICardValidationContext.ForceWarnings](P_Tessa_Cards_Validation_ICardValidationContext_ForceWarnings.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
[Tessa.Platform.ObjectSealedException]
