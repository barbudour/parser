# CurrentUserDataProtectionService.Protect - метод
Осуществляет шифрование данных data
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public byte[] Protect(
    	byte[] data
    )
VB __Копировать
     Public Function Protect ( 
    	data As Byte()
    ) As Byte()
C++ __Копировать
     public:
    virtual array<unsigned char>^ Protect(
    	array<unsigned char>^ data
    ) sealed
F# __Копировать
     abstract Protect : 
            data : byte[] -> byte[] 
    override Protect : 
            data : byte[] -> byte[] 
#### Параметры
data [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Шифруемые данные 
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Массив с зашифрованными данными
#### Реализации
[IDataProtectionService.Protect(Byte[])](M_Tessa_Applications_IDataProtectionService_Protect.htm)  
##  __См. также
#### Ссылки
[CurrentUserDataProtectionService -
](T_Tessa_Applications_CurrentUserDataProtectionService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
