# ICardValidationContext.ForceWarnings - свойство
Признак того, что валидаторы-предупреждения срабатывают даже в том случае,
если они не должны срабатывать, например, на клиенте. Это полезно, если
выполняется валидация на клиенте без валидации на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool ForceWarnings { get; set; }
VB __Копировать
     Property ForceWarnings As Boolean
    	Get
    	Set
C++ __Копировать
    property bool ForceWarnings {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     abstract ForceWarnings : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardValidationContext -
](T_Tessa_Cards_Validation_ICardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
[Tessa.Platform.ObjectSealedException]
