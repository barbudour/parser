# ApplicationInstanceManager - конструктор
Initializes a new instance of the
[ApplicationInstanceManager](T_Tessa_Applications_ApplicationInstanceManager.htm)
class. Создаёт экземпляр класса
[ApplicationInstanceManager](T_Tessa_Applications_ApplicationInstanceManager.htm).
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationInstanceManager(
    	[NotNullAttribute] string applicationName,
    	bool skipRegistration = false
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> applicationName As String,
    	Optional skipRegistration As Boolean = false
    )
C++ __Копировать
     public:
    ApplicationInstanceManager(
    	[NotNullAttribute] String^ applicationName, 
    	bool skipRegistration = false
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] applicationName : string * 
            ?skipRegistration : bool 
    (* Defaults:
            let _skipRegistration = defaultArg skipRegistration false
    *)
    -> ApplicationInstanceManager
#### Параметры
applicationName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Уникальное имя приложения в системе 
skipRegistration
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     if set to true не выполняет регистрацию текущего экземпляра приложения в системе 
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
applicationName is null.  
---|---  
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)|
Параметр является отрицательным числом, отличным от -1, которое представляет
неограниченное время ожидания.  
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
Длина значения параметра более 260 символов.  
[AbandonedMutexException](https://learn.microsoft.com/dotnet/api/system.threading.abandonedmutexexception)|
Ожидание завершено, поскольку поток завершил работу, не освободив мьютекс.Это
исключение не выдается в операционных системах Windows 98 и Windows Millennium
Edition.  
[UnauthorizedAccessException](https://learn.microsoft.com/dotnet/api/system.unauthorizedaccessexception)|
Именованный мьютекс существует, имеет безопасность управления доступом, а
пользователь не имеет прав
[FullControl](https://learn.microsoft.com/dotnet/api/system.security.accesscontrol.mutexrights).  
[IOException](https://learn.microsoft.com/dotnet/api/system.io.ioexception)|
Произошла ошибка Win32.  
[ApplicationException](https://learn.microsoft.com/dotnet/api/system.applicationexception)|
Именованный мьютекс не может быть создан; вероятно, дескриптор ожидания
другого типа имеет то же имя.  
[ObjectDisposedException](https://learn.microsoft.com/dotnet/api/system.objectdisposedexception)|
Текущий экземпляр уже был удален.  
## __См. также
#### Ссылки
[ApplicationInstanceManager -
](T_Tessa_Applications_ApplicationInstanceManager.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
