# ExtensionOrderKey - конструктор
Создаёт экземпляр типа значения с указанием этапа выполнения расширения в
цепочке расширений и порядка выполнения расширения внутри этапа.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ExtensionOrderKey(
    	ExtensionStage stage,
    	int order = 0
    )
VB __Копировать
     Public Sub New ( 
    	stage As ExtensionStage,
    	Optional order As Integer = 0
    )
C++ __Копировать
     public:
    ExtensionOrderKey(
    	ExtensionStage stage, 
    	int order = 0
    )
F# __Копировать
     new : 
            stage : ExtensionStage * 
            ?order : int 
    (* Defaults:
            let _order = defaultArg order 0
    *)
    -> ExtensionOrderKey
#### Параметры
stage [ExtensionStage](T_Tessa_Extensions_ExtensionStage.htm)
    Этап выполнения расширения в цепочке расширений.
order [Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Порядок выполнения расширений внутри этапа. Расширения с меньшим значением порядка выполняются раньше. 
## __См. также
#### Ссылки
[ExtensionOrderKey - ](T_Tessa_Extensions_ExtensionOrderKey.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
