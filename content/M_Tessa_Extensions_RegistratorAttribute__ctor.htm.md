# RegistratorAttribute - конструктор
Создаёт экземпляр класса
[RegistratorAttribute](T_Tessa_Extensions_RegistratorAttribute.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public RegistratorAttribute(
    	ExtensionStage stage = ExtensionStage.AfterPlatform
    )
VB __Копировать
     Public Sub New ( 
    	Optional stage As ExtensionStage = ExtensionStage.AfterPlatform
    )
C++ __Копировать
     public:
    RegistratorAttribute(
    	ExtensionStage stage = ExtensionStage::AfterPlatform
    )
F# __Копировать
     new : 
            ?stage : ExtensionStage 
    (* Defaults:
            let _stage = defaultArg stage ExtensionStage.AfterPlatform
    *)
    -> RegistratorAttribute
#### Параметры
stage [ExtensionStage](T_Tessa_Extensions_ExtensionStage.htm) (Optional)
    Этап выполнения регистратора в цепочке регистрации.
##  __См. также
#### Ссылки
[RegistratorAttribute - ](T_Tessa_Extensions_RegistratorAttribute.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
