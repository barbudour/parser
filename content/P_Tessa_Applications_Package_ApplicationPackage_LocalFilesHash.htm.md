# ApplicationPackage.LocalFilesHash - свойство
Возвращает или задаёт массив байт содержащий значения хеш-кодов доступных
локально файлов.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataMemberAttribute(EmitDefaultValue = false, IsRequired = false)]
    public byte[] LocalFilesHash { get; set; }
VB __Копировать
    <DataMemberAttribute(EmitDefaultValue := false, IsRequired := false)>
    Public Property LocalFilesHash As Byte()
    	Get
    	Set
C++ __Копировать
     public:
    [DataMemberAttribute(EmitDefaultValue = false, IsRequired = false)]
    property array<unsigned char>^ LocalFilesHash {
    	array<unsigned char>^ get ();
    	void set (array<unsigned char>^ value);
    }
F# __Копировать
     [<DataMemberAttribute(EmitDefaultValue = false, IsRequired = false)>]
    member LocalFilesHash : byte[] with get, set
#### Значение свойства
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
##  __Заметки
Для получения значения отдельных хеш-кодов необходимо единый массив разделить
на части равные длине хеш-кода.
##  __См. также
#### Ссылки
[ApplicationPackage - ](T_Tessa_Applications_Package_ApplicationPackage.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
