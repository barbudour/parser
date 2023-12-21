# ApplicationInstanceManager.Register - метод
Выполняет регистрация текущего экземпляра приложения в системе
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void Register()
VB __Копировать
     Public Sub Register
C++ __Копировать
     public:
    void Register()
F# __Копировать
     member Register : unit -> unit 
## __Исключения
[ObjectDisposedException](https://learn.microsoft.com/dotnet/api/system.objectdisposedexception)|
Текущий экземпляр уже был удален.  
---|---  
[AbandonedMutexException](https://learn.microsoft.com/dotnet/api/system.threading.abandonedmutexexception)|
Ожидание завершено, поскольку поток завершил работу, не освободив мьютекс.Это
исключение не выдается в операционных системах Windows 98 и Windows Millennium
Edition.  
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)|
Параметр является отрицательным числом, отличным от -1, которое представляет
неограниченное время ожидания.  
[UnauthorizedAccessException](https://learn.microsoft.com/dotnet/api/system.unauthorizedaccessexception)|
Именованный мьютекс существует, имеет безопасность управления доступом, а
пользователь не имеет прав
[FullControl](https://learn.microsoft.com/dotnet/api/system.security.accesscontrol.mutexrights).  
[IOException](https://learn.microsoft.com/dotnet/api/system.io.ioexception)|
Произошла ошибка Win32.  
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
Длина значения параметра более 260 символов.  
[ApplicationException](https://learn.microsoft.com/dotnet/api/system.applicationexception)|
Именованный мьютекс не может быть создан; вероятно, дескриптор ожидания
другого типа имеет то же имя.  
## __См. также
#### Ссылки
[ApplicationInstanceManager -
](T_Tessa_Applications_ApplicationInstanceManager.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
