# CardCacheHelper.CheckKey - метод
Проверяет заданный ключ на корректность. В случае ошибки бросает исключение.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void CheckKey(
    	string key
    )
VB __Копировать
     Public Shared Sub CheckKey ( 
    	key As String
    )
C++ __Копировать
     public:
    static void CheckKey(
    	String^ key
    )
F# __Копировать
     static member CheckKey : 
            key : string -> unit 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, который требуется проверить на корректность.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Аргумент key равен null.  
---|---  
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)|
Аргумент key содержит строку, имеющую большую длину, чем максимально
допустимая длина
[MaxKeyLength](F_Tessa_Cards_Caching_CardCacheHelper_MaxKeyLength.htm).  
## __См. также
#### Ссылки
[CardCacheHelper - ](T_Tessa_Cards_Caching_CardCacheHelper.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
