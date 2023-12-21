# IErrorLog.Execute - метод
Выполняет действие validationAction для добавления ошибки в лог
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void Execute(
    	[NotNullAttribute] Action<IValidationResultBuilder> validationAction
    )
VB __Копировать
     Sub Execute ( 
    	<NotNullAttribute> validationAction As Action(Of IValidationResultBuilder)
    )
C++ __Копировать
     void Execute(
    	[NotNullAttribute] Action<IValidationResultBuilder^>^ validationAction
    )
F# __Копировать
     abstract Execute : 
            [<NotNullAttribute>] validationAction : Action<IValidationResultBuilder> -> unit 
#### Параметры
validationAction
[Action](https://learn.microsoft.com/dotnet/api/system.action-1)<[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)>
     Действие предоставляющее информацию о возникшей исключительной ситуации 
## __См. также
#### Ссылки
[IErrorLog - ](T_Tessa_Applications_IErrorLog.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
