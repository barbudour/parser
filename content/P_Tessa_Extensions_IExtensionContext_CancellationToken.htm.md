# IExtensionContext.CancellationToken - свойство
Объект, посредством которого можно отменить асинхронную задачу.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    CancellationToken CancellationToken { get; set; }
VB __Копировать
     Property CancellationToken As CancellationToken
    	Get
    	Set
C++ __Копировать
    property CancellationToken CancellationToken {
    	CancellationToken get ();
    	void set (CancellationToken value);
    }
F# __Копировать
     abstract CancellationToken : CancellationToken with get, set
#### Значение свойства
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
##  __Заметки
Не изменяйте значение этого свойства в процессе выполнения расширений.
##  __См. также
#### Ссылки
[IExtensionContext - ](T_Tessa_Extensions_IExtensionContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
